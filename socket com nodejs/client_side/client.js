//Importa o módulo NET do node para comunicação TCP
const net = require('net')
const JsonSocket =  require('json-socket')
const prompt = require('prompt-sync')();
//Vai criar um Socket novo e conectalo em uma porta
const client = new JsonSocket(new net.Socket());
client.connect(7777, '127.0.0.1', () => {
	console.log('Conectado!')

	client.sendMessage({
		num1: parseInt(prompt('Digite o 1º número da soma: ')),
		num2: parseInt(prompt('Digite o 2º número da soma: '))
	});

	client.on('message', message => {
		console.log(`O resultado da soma é: ${message.result}`)
	})
})