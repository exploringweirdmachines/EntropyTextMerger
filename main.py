import math
from collections import defaultdict

class TextChunker:
    """
    Orchestrates the process of calculating next byte entropies and chunking text
    based on patch boundaries.
    """

    def __init__(self, language_model=None, global_threshold=None, relative_threshold=None):
        self.global_threshold = global_threshold
        self.relative_threshold = relative_threshold
        self.byte_pair_probs = None
        self.language_model = language_model if language_model else self._default_language_model

    def train(self, corpus):
        """
        Trains the language model on the given corpus to estimate byte pair probabilities.
        """
        byte_counts = defaultdict(int)
        pair_counts = defaultdict(int)

        for text in corpus:
            encoded_text = text.encode('utf-8')
            for byte in encoded_text:
                byte_counts[byte] += 1
            for i in range(len(encoded_text) - 1):
                pair = (encoded_text[i], encoded_text[i + 1])
                pair_counts[pair] += 1

        total_bytes = sum(byte_counts.values())
        self.byte_pair_probs = {}
        for pair, count in pair_counts.items():
            # Calculate the probability of the second byte given the first
            first_byte_count = byte_counts[pair[0]]
            if first_byte_count > 0:
                self.byte_pair_probs[pair] = count / first_byte_count

    def _default_language_model(self, previous_bytes, next_byte):
        """
        Uses the trained byte pair probabilities to estimate the probability of the next byte.
        """
        if not previous_bytes:
            # If no previous bytes, use a uniform distribution or some prior
            return 1 / 256.0

        previous_byte = previous_bytes[-1]
        prob = self.byte_pair_probs.get((previous_byte, next_byte), 0.00001) # Add a small default prob
        return prob

    def calculate_entropies(self, text):
        """
        Calculates the next byte entropies for a given text using the trained language model.
        """
        entropies = []
        encoded_text = text.encode('utf-8')
        for i in range(1, len(encoded_text)):
            previous_bytes = list(encoded_text[:i])
            current_byte = encoded_text[i]
            prob = self.language_model(previous_bytes, current_byte)
            if prob > 0:
                entropy = -prob * math.log2(prob)
                entropies.append(entropy)
        return entropies

    def identify_patch_boundaries(self, entropies):
        """
        Identifies patch boundaries in a sequence of byte entropies using two methods.
        """
        global_boundaries = []
        relative_boundaries = []

        # Method 1: Global Threshold
        if self.global_threshold is not None:
            for i, entropy in enumerate(entropies):
              if entropy > self.global_threshold:
                 global_boundaries.append(i+1) # Add 1 to match the original index in text

        # Method 2: Approximate Monotonic Constraint
        if self.relative_threshold is not None and len(entropies) > 1:
            for i in range(1, len(entropies)):
              if entropies[i] - entropies[i - 1] > self.relative_threshold:
                relative_boundaries.append(i+1) # Add 1 to match the original index in text

        return global_boundaries, relative_boundaries

    def chunk_text(self, text, boundaries):
        """Chunks a text string based on provided boundary indices."""
        chunks = []
        sorted_boundaries = sorted(list(set(boundaries)))
        start_index = 0
        for boundary in sorted_boundaries:
            chunks.append(text[start_index:boundary]) # Changed to boundary without +1 to match results
            start_index = boundary
        if start_index < len(text):
            chunks.append(text[start_index:])
        return chunks

    def text_to_hex(self, text):
        return text.encode('utf-8').hex()

    def chunk(self, text):
        entropies = self.calculate_entropies(text)
        global_boundaries, relative_boundaries = self.identify_patch_boundaries(entropies)
        combined_boundaries = sorted(list(set(global_boundaries + relative_boundaries)))
        chunks = self.chunk_text(text, combined_boundaries)
        hex_chunks = [self.text_to_hex(chunk) for chunk in chunks]

        return {
            "text": text,
            "entropies": entropies,
            "global_boundaries": global_boundaries,
            "relative_boundaries": relative_boundaries,
            "combined_boundaries": combined_boundaries,
            "chunks": chunks,
            "hex_chunks": hex_chunks,
        }

# --- Example Usage of the TextChunker Class with Training ---
corpus = [
    "This is the first document for training.",
    "Another example document to train the model.",
    "Training helps in understanding text patterns.",
    "More training data for better probability estimation."
]

# Initialize TextChunker
chunker = TextChunker(global_threshold=0.5, relative_threshold=0.03)

# Train the chunker on the corpus
chunker.train(corpus)

example_string = "This is a new string to be chunked after training. It should reflect the learned probabilities."
result = chunker.chunk(example_string)

print("Chunking results after training:")
print(f"  Text: {result['text']}")
print(f"  Entropies: {['{:.2f}'.format(e) for e in result['entropies']]}")
print(f"  Global Boundaries: {result['global_boundaries']}")
print(f"  Relative Boundaries: {result['relative_boundaries']}")
print(f"  Combined Boundaries: {result['combined_boundaries']}")
print("  Text Chunks:")
for i, chunk in enumerate(result['chunks']):
    print(f"    Chunk {i+1}: '{chunk}'")
    print(f"      Hex: {result['hex_chunks'][i]}")
print("-" * 50)

# Example with different thresholds after training
chunker_diff_thresh = TextChunker(global_threshold=0.8, relative_threshold=0.08)
chunker_diff_thresh.train(corpus)
result_diff_thresh = chunker_diff_thresh.chunk(example_string)

print("Chunking results with different thresholds after training:")
print(f"  Text: {result_diff_thresh['text']}")
print(f"  Entropies: {['{:.2f}'.format(e) for e in result_diff_thresh['entropies']]}")
print(f"  Global Boundaries: {result_diff_thresh['global_boundaries']}")
print(f"  Relative Boundaries: {result_diff_thresh['relative_boundaries']}")
print(f"  Combined Boundaries: {result_diff_thresh['combined_boundaries']}")
print("  Text Chunks:")
for i, chunk in enumerate(result_diff_thresh['chunks']):
    print(f"    Chunk {i+1}: '{chunk}'")
    print(f"      Hex: {result_diff_thresh['hex_chunks'][i]}")
print("-" * 50)


# Example with different thresholds after training
chunker_diff_thresh = TextChunker(global_threshold=0.5)
chunker_diff_thresh.train(corpus)
result_diff_thresh = chunker_diff_thresh.chunk(example_string)

print("Chunking results with different thresholds after training:")
print(f"  Text: {result_diff_thresh['text']}")
print(f"  Entropies: {['{:.2f}'.format(e) for e in result_diff_thresh['entropies']]}")
print(f"  Global Boundaries: {result_diff_thresh['global_boundaries']}")
print("  Text Chunks:")
for i, chunk in enumerate(result_diff_thresh['chunks']):
    print(f"    Chunk {i+1}: '{chunk}'")
    print(f"      Hex: {result_diff_thresh['hex_chunks'][i]}")
print("-" * 50)
