from code_generator.new_visitor import generate_ir
from running import run

print("Введите название cpp файла:")
cpp_file = input()

print(f"\nГенерируем ll-файл для {cpp_file}")

print(f"~~ Input file: {cpp_file}")
ll_file = cpp_file[:-3] + ".ll"
print(f"~~ Output file: {ll_file}")

generate_ir(cpp_file, ll_file)

print("\nЗапускаем ll-файл:")
result = run(ll_file)
print(f"Program {ll_file} exits with code {result}\n\nResult of program:")