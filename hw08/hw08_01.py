from collections import Counter, deque


class HuffmanEncoder:
    def __init__(self, text):
        self.text = str(text)
        self.encoding_table = {}

    def huffman_tree(self):
        symbol_frequency = Counter(self.text)
        sorted_symbols = deque(sorted(symbol_frequency.items(), key=lambda item: item[1]))
        if len(sorted_symbols) != 1:
            while len(sorted_symbols) > 1:
                freq = sorted_symbols[0][1] + sorted_symbols[1][1]
                tree_node = {0: sorted_symbols.popleft()[0],
                             1: sorted_symbols.popleft()[0]}
                for index, arguments in enumerate(sorted_symbols):
                    if freq > arguments[1]:
                        continue
                    else:
                        sorted_symbols.insert(index, (tree_node, freq))
                        break
                else:
                    sorted_symbols.append((tree_node, freq))
        else:
            freq = sorted_symbols[0][1]
            tree_node = {0: sorted_symbols.popleft()[0], 1: None}
            sorted_symbols.append((tree_node, freq))

        return sorted_symbols[0][0]

    def huffman_encoding_table(self, tree, path=''):
        if not isinstance(tree, dict):
            self.encoding_table[tree] = path
        else:
            self.huffman_encoding_table(tree[0], path=f'{path}0')
            self.huffman_encoding_table(tree[1], path=f'{path}1')
        return self.encoding_table

    def huffman_encoding(self):
        if self.encoding_table == {}:
            self.huffman_encoding_table(self.huffman_tree())
        encoded_text = ''
        for i in self.text:
            encoded_text += self.encoding_table[i] + ' '
        return encoded_text

    def huffman_decoding(self):
        decoded_text = ''
        for item in self.huffman_encoding().split(' '):
            for key, value in self.encoding_table.items():
                if value == item:
                    decoded_text += key
        return decoded_text


my_string = HuffmanEncoder("beep boop beer!")

print(my_string.huffman_encoding())
print(my_string.encoding_table)
print(my_string.huffman_decoding())


my_string_2 = HuffmanEncoder("hello world")

print(my_string_2.huffman_encoding())
print(my_string_2.encoding_table)
print(my_string_2.huffman_decoding())
