import os
def main():
  nombre: os.getenv("USERNAME")
  print(f"hello platzi {nombre} gh actions")

if __name__ == "__main__":
  main()
