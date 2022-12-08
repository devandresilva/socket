//Importa o módulo NET do node para comunicação TCP, e o FS para Uso de arquivos
const server = require('net').createServer();
const JsonSocket =  require('json-socket')

server.listen(7777, '127.0.0.1')
console.log('Aguadando conexão...')

server.on('connection', socket => {
	console.log('Cliente conectado!');

	socket = new JsonSocket(socket);

	socket.on('message', message => {
		let result = message.num1 + message.num2;
		socket.sendEndMessage({result: result})
	})

	socket.on('end', () => {
		console.log('Cliente desconectou!')
	})
})