Classe de utilitários de arquivos
Visão geral
Este projeto fornece uma classe utilitária, Files, que simplifica várias operações de arquivo e pasta, como copiar, renomear, mover, criar e excluir arquivos e diretórios. A classe é implementada em Python e inclui vários métodos úteis para gerenciamento de arquivos.

Características
A Filesclasse inclui os seguintes recursos:

Copiar arquivos
Copie um arquivo de um diretório para outro.

Criar pasta e copiar arquivos
Crie uma nova pasta e copie um arquivo para ela.

Criar pastas
Crie uma nova pasta se ela não existir.

Renomear arquivos
Renomeie todos os arquivos em um diretório especificado para um novo formato de nomenclatura.

Renomear um único arquivo
Renomeie um único arquivo de um nome antigo para um novo nome.

Verificar presença de arquivo
Aguarde até que um arquivo com uma extensão específica apareça em um diretório.

Excluir arquivos ou pastas
Exclua arquivos ou diretórios e seus conteúdos.

Mover arquivos
Mova arquivos para um destino especificado.

Criar arquivos de texto
Crie um arquivo de texto vazio.

Converter formato de arquivo
Renomeie um arquivo para alterar seu formato.

Ajustar conteúdo do arquivo
Substitua conteúdo específico em um arquivo e grave o conteúdo modificado em outro arquivo.

Instalação
Para usar esta classe, certifique-se de que o Python 3.x esteja instalado no seu sistema. Clone o repositório ou copie o script para o seu projeto.

Uso
Inicialização
Para usar a classe, importe-a para seu script e crie uma instância:

Pitão

Copiar código
from files import Files

files = Files()
Métodos de exemplo
Copiar um arquivo

Pitão

Copiar código
files.copy(path="source_path", file="file_name.txt", destiny="destination_path")
Crie uma pasta e copie um arquivo

Pitão

Copiar código
files.craeteForlderAndCopy(
    name_folder="new_folder",
    path="source_path",
    file="file_name.txt",
    destiny="destination_path"
)
Renomear todos os arquivos em uma pasta

Pitão

Copiar código
files.renameFiles(
    path="folder_path",
    files=["new_name1", "new_name2"],
    extension="txt"
)
Verificar a presença do arquivo

Pitão

Copiar código
files.check_file_with_extension(directory="folder_path", extension=".txt")
Excluir um arquivo ou pasta

Pitão

Copiar código
files.delete(path="file_or_folder_path")
Ajustar conteúdo do arquivo

Pitão

Copiar código
files.adjust_bar(
    path="source_file.txt",
    path_destiny="destination_file.txt",
    old_replace="\\\\\\",
    new_replace="\\\\"
)
Resumo dos métodos
Método	Descrição
copy	Copia um arquivo para um destino especificado.
craeteForlderAndCopy	Cria uma pasta e copia um arquivo para ela.
create	Cria uma pasta se ela não existir.
renameFiles	Renomeia todos os arquivos em uma pasta especificada.
rename_one_file	Renomeia um único arquivo.
check_file_with_extension	Aguarda que um arquivo com uma extensão específica apareça em uma pasta.
delete	Exclui arquivos ou pastas.
move_file	Move um arquivo para um novo local.
create_text	Cria um arquivo de texto vazio.
convert_file	Altera o formato de um arquivo renomeando-o.
adjust_bar	Substitui conteúdo específico em um arquivo e o grava em outro arquivo.
Contribuindo
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um pull request ou criar um issue.

Autor: Kaique Batista Ramos
Versão: 1.1.5
