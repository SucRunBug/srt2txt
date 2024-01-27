# 传递命令行参数
import sys
# 检查命令行参数数量
if len(sys.argv) != 2:
    print("用法: python3 srtShowup.py <文件名>")
    sys.exit(1)  # 退出脚本，返回非零表示错误
file_name = sys.argv[1]

def process_str_file(input_file):
    # 打开输入文件和输出文件
    with open(input_file, 'r', encoding='utf-8') as input_file:
        # 读取输入文件的每一行
        lines = input_file.readlines()

        # 初始化一个变量来存储合并的字幕行
        merged_lines = []

        # 遍历每一行
        for line in lines:
            # 检查是否是字幕序号行或 时间线行
            if not line.strip().isdigit() and '-->' not in line:
                # 如果不是字幕序号行或时间线行，则将其添加到合并的字幕行中
                merged_line = line.strip()
                # 去掉空行
                if merged_line:
                    merged_line = merged_line + '，'
                    merged_lines.append(merged_line)
                    
        for item in merged_lines:       
            print(item, end='')
# 使用示例
# process_str_file('away.srt')
process_str_file(file_name)
