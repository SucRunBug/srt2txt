# 传递命令行参数
import sys
# 检查命令行参数数量
if len(sys.argv) != 2:
    print("用法: python3 srt2txt.py <文件名>")
    sys.exit(1)  # 退出脚本，返回非零表示错误
file_name = sys.argv[1]

def process_str_file(input_file, output_file):
    # 打开输入文件和输出文件
    with open(input_file, 'r', encoding='utf-8') as input_file, open(output_file, 'w', encoding='utf-8') as output_file:
        # 读取输入文件的每一行
        lines = input_file.readlines()

        # 初始化一个变量来存储合并的字幕行
        merged_lines = []

        # 遍历每一行
        for line in lines:
            # 检查是否是字幕序号行或时间线行
            if not line.strip().isdigit() and '-->' not in line:
                # 如果不是字幕序号行或时间线行，则将其添加到合并的字幕行中
                merged_line = line.strip()
                if merged_line:
                    merged_lines.append(merged_line)

        # 将合并的字幕行写入输出文件
        output_file.write('，'.join(merged_lines))

# 使用示例
process_str_file(file_name, 'output_file.txt')
