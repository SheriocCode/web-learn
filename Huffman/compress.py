import os
import heapq
from collections import Counter

# 定义 Huffman 树节点
class HuffmanNode:
    def __init__(self, byte, freq):
        self.byte = byte
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# 构建 Huffman 树
def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(byte, freq) for byte, freq in freq_dict.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

# 生成 Huffman 编码表
def generate_huffman_codes(node, prefix="", code_dict=None):
    if code_dict is None:
        code_dict = {}
    if node is not None:
        if node.byte is not None:
            code_dict[node.byte] = prefix
        generate_huffman_codes(node.left, prefix + "0", code_dict)
        generate_huffman_codes(node.right, prefix + "1", code_dict)
    return code_dict

# 读取 BMP 文件内容
def read_bmp_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# 压缩文件内容
def compress_file_content(file_content):
    freq_dict = Counter(file_content)
    huffman_tree = build_huffman_tree(freq_dict)
    huffman_codes = generate_huffman_codes(huffman_tree)
    encoded_data = ''.join(huffman_codes[byte] for byte in file_content)
    return encoded_data, huffman_tree

# 将编码后的数据转换为字节流
def encode_to_bytes(encoded_data):
    padding = 8 - (len(encoded_data) % 8)
    if padding != 8:
        encoded_data += '0' * padding
    byte_array = bytearray()
    for i in range(0, len(encoded_data), 8):
        byte = int(encoded_data[i:i+8], 2)
        byte_array.append(byte)
    return byte_array

# 序列化 Huffman 树
def serialize_huffman_tree(node):
    if node is None:
        return b''
    if node.byte is not None:
        # 叶节点标记 \x01
        return b'\x01' + bytes([node.byte])
    else:
        # 非叶节点标记 \x00
        return b'\x00' + serialize_huffman_tree(node.left) + serialize_huffman_tree(node.right)

# 反序列化 Huffman 树
def deserialize_huffman_tree(serialized_tree):
    def _deserialize():
        nonlocal index
        marker = serialized_tree[index]
        index += 1
        if marker == 0:  # 内部节点
            left = _deserialize()
            right = _deserialize()
            node = HuffmanNode(None, left.freq + right.freq)
            node.left = left
            node.right = right
            return node
        else:  # 叶子节点
            byte = serialized_tree[index]
            index += 1
            return HuffmanNode(byte, 1)

    index = 0
    return _deserialize()

# 解码压缩数据
def decode_compressed_data(encoded_bytes, huffman_tree):
    encoded_data = ''.join(f'{byte:08b}' for byte in encoded_bytes)
    padding = 8 - (len(encoded_data) % 8)
    if padding != 8:
        encoded_data = encoded_data[:-padding]

    decoded_data = []
    current_node = huffman_tree
    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.byte is not None:  # 到达叶子节点
            decoded_data.append(current_node.byte)
            current_node = huffman_tree  # 重置到根节点
    return bytes(decoded_data)

# 写入压缩文件
def write_compressed_file(output_path, serialized_tree, compressed_data):
    with open(output_path, "wb") as file:
        file.write(len(serialized_tree).to_bytes(4, byteorder="big"))
        file.write(serialized_tree)
        file.write(len(compressed_data).to_bytes(4, byteorder="big"))
        file.write(compressed_data)

# 读取压缩文件
def read_compressed_file(input_path):
    with open(input_path, "rb") as file:
        tree_length = int.from_bytes(file.read(4), byteorder="big")
        serialized_tree = file.read(tree_length)
        data_length = int.from_bytes(file.read(4), byteorder="big")
        compressed_data = file.read(data_length)
    return serialized_tree, compressed_data


# 示例：读取 BMP 文件并压缩
file_path = "/workspaces/web-learn/Huffman/pic/picture.bmp"
file_content = read_bmp_file(file_path)
encoded_data, huffman_tree = compress_file_content(file_content)
compressed_data = encode_to_bytes(encoded_data)
serialized_tree = serialize_huffman_tree(huffman_tree)
output_path = "compressed.huf"
write_compressed_file(output_path, serialized_tree, compressed_data)
print(f"BMP 文件已压缩并保存为 {output_path}")

# 示例：解码压缩文件
compressed_file_path = "compressed.huf"
serialized_tree, compressed_data = read_compressed_file(compressed_file_path)
huffman_tree = deserialize_huffman_tree(serialized_tree)
decoded_data = decode_compressed_data(compressed_data, huffman_tree)
output_path = "decompressed.bmp"
with open(output_path, "wb") as file:
    file.write(decoded_data)
print(f"解码后的 BMP 文件已保存为 {output_path}")


# 计算文件大小
def get_file_size(file_path):
    return os.path.getsize(file_path)

# 计算压缩率和节省的存储空间
def calculate_compression_metrics(original_size, compressed_size):
    compression_rate = compressed_size / original_size
    saved_space = 1 - compression_rate
    return compression_rate, saved_space

# 输出详细信息
def print_compression_details(original_file_path, compressed_file_path):
    # 获取压缩前后的文件大小
    original_size = get_file_size(original_file_path)
    compressed_size = get_file_size(compressed_file_path)

    # 计算压缩率和节省的存储空间
    compression_rate, saved_space = calculate_compression_metrics(original_size, compressed_size)

    # 输出详细信息
    print(f"原始文件路径: {original_file_path}")
    print(f"压缩文件路径: {compressed_file_path}")
    print(f"原始文件大小: {original_size} 字节")
    print(f"压缩文件大小: {compressed_size} 字节")
    print(f"压缩率: {compression_rate:.2f} ({compressed_size / original_size * 100:.2f}%)")
    print(f"节省的存储空间: {saved_space:.2f} ({saved_space * 100:.2f}%)")
    print(f"节省的字节数: {original_size - compressed_size} 字节")

# 示例：读取 BMP 文件并压缩
file_path = "/workspaces/web-learn/Huffman/pic/picture.bmp"
file_content = read_bmp_file(file_path)
encoded_data, huffman_tree = compress_file_content(file_content)
compressed_data = encode_to_bytes(encoded_data)
serialized_tree = serialize_huffman_tree(huffman_tree)

# 将压缩后的数据和 Huffman 树结构写入文件
output_path = "compressed.huf"
write_compressed_file(output_path, serialized_tree, compressed_data)

print(f"BMP 文件已压缩并保存为 {output_path}")

# 输出压缩前后的详细信息
print_compression_details(file_path, output_path)