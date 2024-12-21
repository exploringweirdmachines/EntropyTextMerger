# EntropyTextMerger
Example entropy based text chunker. Inspired by Byte Latent Transformer paper from META, and Andrej Karpathy's BPE Tokenizer.

# Usage
```bash
python main.py
```
## Output

```bash
Chunking results after training:
  Text: This is a new string to be chunked after training. It should reflect the learned probabilities.
  Entropies: ['0.50', '0.46', '0.38', '0.52', '0.31', '0.38', '0.52', '0.00', '0.31', '0.00', '0.00', '0.00', '0.00', '0.00', '0.52', '0.40', '0.00', '0.47', '0.50', '0.31', '0.52', '0.21', '0.33', '0.20', '0.53', '0.50', '0.00', '0.00', '0.00', '0.53', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.40', '0.50', '0.52', '0.52', '0.40', '0.52', '0.53', '0.47', '0.45', '0.47', '0.50', '0.50', '0.00', '0.00', '0.00', '0.46', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.28', '0.00', '0.00', '0.50', '0.00', '0.00', '0.46', '0.52', '0.40', '0.26', '0.50', '0.00', '0.50', '0.00', '0.00', '0.28', '0.00', '0.00', '0.00', '0.31', '0.50', '0.28', '0.33', '0.53', '0.31', '0.53', '0.25', '0.50', '0.25', '0.32', '0.00', '0.25', '0.40']
  Global Boundaries: [4, 7, 15, 21, 25, 30, 40, 41, 43, 44, 69, 85, 87]
  Relative Boundaries: [4, 6, 7, 9, 15, 18, 19, 21, 23, 25, 30, 38, 39, 43, 48, 53, 62, 65, 68, 69, 72, 74, 77, 81, 82, 84, 85, 87, 89, 91, 93, 94]
  Combined Boundaries: [4, 6, 7, 9, 15, 18, 19, 21, 23, 25, 30, 38, 39, 40, 41, 43, 44, 48, 53, 62, 65, 68, 69, 72, 74, 77, 81, 82, 84, 85, 87, 89, 91, 93, 94]
  Text Chunks:
    Chunk 1: 'This'
      Hex: 54686973
    Chunk 2: ' i'
      Hex: 2069
    Chunk 3: 's'
      Hex: 73
    Chunk 4: ' a'
      Hex: 2061
    Chunk 5: ' new s'
      Hex: 206e65772073
    Chunk 6: 'tri'
      Hex: 747269
    Chunk 7: 'n'
      Hex: 6e
    Chunk 8: 'g '
      Hex: 6720
    Chunk 9: 'to'
      Hex: 746f
    Chunk 10: ' b'
      Hex: 2062
    Chunk 11: 'e chu'
      Hex: 6520636875
    Chunk 12: 'nked aft'
      Hex: 6e6b656420616674
    Chunk 13: 'e'
      Hex: 65
    Chunk 14: 'r'
      Hex: 72
    Chunk 15: ' '
      Hex: 20
    Chunk 16: 'tr'
      Hex: 7472
    Chunk 17: 'a'
      Hex: 61
    Chunk 18: 'inin'
      Hex: 696e696e
    Chunk 19: 'g. It'
      Hex: 672e204974
    Chunk 20: ' should r'
      Hex: 2073686f756c642072
    Chunk 21: 'efl'
      Hex: 65666c
    Chunk 22: 'ect'
      Hex: 656374
    Chunk 23: ' '
      Hex: 20
    Chunk 24: 'the'
      Hex: 746865
    Chunk 25: ' l'
      Hex: 206c
    Chunk 26: 'ear'
      Hex: 656172
    Chunk 27: 'ned '
      Hex: 6e656420
    Chunk 28: 'p'
      Hex: 70
    Chunk 29: 'ro'
      Hex: 726f
    Chunk 30: 'b'
      Hex: 62
    Chunk 31: 'ab'
      Hex: 6162
    Chunk 32: 'il'
      Hex: 696c
    Chunk 33: 'it'
      Hex: 6974
    Chunk 34: 'ie'
      Hex: 6965
    Chunk 35: 's'
      Hex: 73
    Chunk 36: '.'
      Hex: 2e
--------------------------------------------------
Chunking results with different thresholds after training:
  Text: This is a new string to be chunked after training. It should reflect the learned probabilities.
  Entropies: ['0.50', '0.46', '0.38', '0.52', '0.31', '0.38', '0.52', '0.00', '0.31', '0.00', '0.00', '0.00', '0.00', '0.00', '0.52', '0.40', '0.00', '0.47', '0.50', '0.31', '0.52', '0.21', '0.33', '0.20', '0.53', '0.50', '0.00', '0.00', '0.00', '0.53', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.40', '0.50', '0.52', '0.52', '0.40', '0.52', '0.53', '0.47', '0.45', '0.47', '0.50', '0.50', '0.00', '0.00', '0.00', '0.46', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.28', '0.00', '0.00', '0.50', '0.00', '0.00', '0.46', '0.52', '0.40', '0.26', '0.50', '0.00', '0.50', '0.00', '0.00', '0.28', '0.00', '0.00', '0.00', '0.31', '0.50', '0.28', '0.33', '0.53', '0.31', '0.53', '0.25', '0.50', '0.25', '0.32', '0.00', '0.25', '0.40']
  Global Boundaries: []
  Relative Boundaries: [4, 7, 9, 15, 18, 21, 23, 25, 30, 38, 39, 43, 53, 62, 65, 68, 72, 74, 77, 81, 82, 85, 87, 89, 93, 94]
  Combined Boundaries: [4, 7, 9, 15, 18, 21, 23, 25, 30, 38, 39, 43, 53, 62, 65, 68, 72, 74, 77, 81, 82, 85, 87, 89, 93, 94]
  Text Chunks:
    Chunk 1: 'This'
      Hex: 54686973
    Chunk 2: ' is'
      Hex: 206973
    Chunk 3: ' a'
      Hex: 2061
    Chunk 4: ' new s'
      Hex: 206e65772073
    Chunk 5: 'tri'
      Hex: 747269
    Chunk 6: 'ng '
      Hex: 6e6720
    Chunk 7: 'to'
      Hex: 746f
    Chunk 8: ' b'
      Hex: 2062
    Chunk 9: 'e chu'
      Hex: 6520636875
    Chunk 10: 'nked aft'
      Hex: 6e6b656420616674
    Chunk 11: 'e'
      Hex: 65
    Chunk 12: 'r tr'
      Hex: 72207472
    Chunk 13: 'aining. It'
      Hex: 61696e696e672e204974
    Chunk 14: ' should r'
      Hex: 2073686f756c642072
    Chunk 15: 'efl'
      Hex: 65666c
    Chunk 16: 'ect'
      Hex: 656374
    Chunk 17: ' the'
      Hex: 20746865
    Chunk 18: ' l'
      Hex: 206c
    Chunk 19: 'ear'
      Hex: 656172
    Chunk 20: 'ned '
      Hex: 6e656420
    Chunk 21: 'p'
      Hex: 70
    Chunk 22: 'rob'
      Hex: 726f62
    Chunk 23: 'ab'
      Hex: 6162
    Chunk 24: 'il'
      Hex: 696c
    Chunk 25: 'itie'
      Hex: 69746965
    Chunk 26: 's'
      Hex: 73
    Chunk 27: '.'
      Hex: 2e
--------------------------------------------------
Chunking results with different thresholds after training:
  Text: This is a new string to be chunked after training. It should reflect the learned probabilities.
  Entropies: ['0.50', '0.46', '0.38', '0.52', '0.31', '0.38', '0.52', '0.00', '0.31', '0.00', '0.00', '0.00', '0.00', '0.00', '0.52', '0.40', '0.00', '0.47', '0.50', '0.31', '0.52', '0.21', '0.33', '0.20', '0.53', '0.50', '0.00', '0.00', '0.00', '0.53', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.40', '0.50', '0.52', '0.52', '0.40', '0.52', '0.53', '0.47', '0.45', '0.47', '0.50', '0.50', '0.00', '0.00', '0.00', '0.46', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.28', '0.00', '0.00', '0.50', '0.00', '0.00', '0.46', '0.52', '0.40', '0.26', '0.50', '0.00', '0.50', '0.00', '0.00', '0.28', '0.00', '0.00', '0.00', '0.31', '0.50', '0.28', '0.33', '0.53', '0.31', '0.53', '0.25', '0.50', '0.25', '0.32', '0.00', '0.25', '0.40']
  Global Boundaries: [4, 7, 15, 21, 25, 30, 40, 41, 43, 44, 69, 85, 87]
  Text Chunks:
    Chunk 1: 'This'
      Hex: 54686973
    Chunk 2: ' is'
      Hex: 206973
    Chunk 3: ' a new s'
      Hex: 2061206e65772073
    Chunk 4: 'tring '
      Hex: 7472696e6720
    Chunk 5: 'to b'
      Hex: 746f2062
    Chunk 6: 'e chu'
      Hex: 6520636875
    Chunk 7: 'nked after'
      Hex: 6e6b6564206166746572
    Chunk 8: ' '
      Hex: 20
    Chunk 9: 'tr'
      Hex: 7472
    Chunk 10: 'a'
      Hex: 61
    Chunk 11: 'ining. It should reflect '
      Hex: 696e696e672e2049742073686f756c64207265666c65637420
    Chunk 12: 'the learned prob'
      Hex: 746865206c6561726e65642070726f62
    Chunk 13: 'ab'
      Hex: 6162
    Chunk 14: 'ilities.'
      Hex: 696c69746965732e
```
