# Baixando as dependências

Para esse projeto foi necessário a instalação de dois pacotes do nodeJS, o 'prompt-sync' (para que se pudesse obter entradas do usuário no client-side) e o 'json-scoket' para transferência de dados no formato JSON através de do socket usando comunicação TCP.

Código de instlação das dependencias:

npm install json-socket

npm install prompt-sync

# Rodando o projeto

* Para rodar o lado do servidor:
Com terminal na pasta /server_side executar o comando:
node server.js

* Para rodar o lado do cliente:
Com terminal na pasta /client_side executar o comando:
node client.js

# Funcionamento
1. Ao rodar o server ele vai aguardar conexão
2. Ao rodar ao cliente ele vai se conectar ao servidor e informar que foi conectado/o mesmo ocorrer do lado do server.
3. O cliente vai pedir duas entradas do usuário pedindo dois valores numéricos e vai enviar esses dados por server.
4. Ao chegar no servidor esses números serão somados e o resultado é retornado para o cliente e a conexão com o cliente é encerrada.
5. O cliente recebe o resultado e o mesmo é mostrado na tela.