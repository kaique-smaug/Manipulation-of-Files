Em andamento: Irei alimentar ese repositório constantemente.

Files Class
Descrição
A classe Files oferece uma série de métodos úteis para manipulação de arquivos e diretórios em Python. Com ela, você pode copiar arquivos, criar pastas, renomear arquivos em massa, verificar a presença de arquivos em um diretório e excluir arquivos ou pastas.

Funcionalidades
Cópia de Arquivos: Copie arquivos de um diretório para outro, preservando metadados.
Criação de Pastas: Crie novas pastas, com a opção de copiar arquivos imediatamente após a criação.
Renomeação de Arquivos: Renomeie todos os arquivos em um diretório, aplicando uma nova nomenclatura e extensão.
Verificação de Arquivos: Monitore um diretório para verificar quando um arquivo com uma extensão específica estiver presente.
Exclusão de Arquivos/Pastas: Exclua arquivos individuais ou pastas inteiras.
Como Utilizar
Instalação
Certifique-se de que as bibliotecas shutil, time, e os estejam instaladas. Todas essas bibliotecas são nativas do Python.

Exemplo de Uso
python
Copiar código
from files import Files

# Instanciar a classe
file_manager = Files()

# Copiar um arquivo
file_manager.copy(path='/caminho/origem', file='arquivo.txt', destiny='/caminho/destino')

# Criar uma pasta e copiar um arquivo para ela
file_manager.craeteForlderAndCopy(name_folder='minha_pasta', path='/caminho/origem', file='arquivo.txt', destiny='/caminho/destino')

# Criar uma nova pasta
file_manager.create(name_folder='nova_pasta')

# Renomear arquivos em um diretório
file_manager.renameFiles(path='/caminho/arquivos', files=['novo_nome1', 'novo_nome2'], extension='txt')

# Verificar se um arquivo com uma determinada extensão está presente em um diretório
file_manager.checkFileWithExtension(directory='/caminho/para/verificar', extension='.txt')

# Excluir um arquivo ou pasta
file_manager.delete(path='/caminho/para/excluir')
Explicação dos Métodos
copy(path, file, destiny): Copia um arquivo especificado de um diretório para outro.
craeteForlderAndCopy(name_folder, path, file, destiny): Cria uma nova pasta e copia um arquivo para um diretório de destino.
create(name_folder): Cria uma nova pasta se ela não existir.
renameFiles(path, files, extension): Renomeia todos os arquivos em um diretório, aplicando novos nomes e uma extensão especificada.
checkFileWithExtension(directory, extension): Verifica continuamente se um arquivo com uma extensão específica está presente em um diretório.
delete(path): Exclui um arquivo ou diretório especificado.
Requisitos
Python 3.x
Módulos: shutil, time, os
