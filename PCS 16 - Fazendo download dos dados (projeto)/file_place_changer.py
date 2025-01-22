import shutil
from pathlib import Path

# Defina o caminho do arquivo que você deseja mover
source = Path("foo")

# Defina o caminho para o diretório de destino
destination = Path("foo")

# Mova o arquivo
shutil.move(str(source), str(destination))

print("Arquivo movido com sucesso!")
