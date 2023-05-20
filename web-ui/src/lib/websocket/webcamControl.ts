import { io } from 'socket.io-client';

const socket = io('ws://localhost:5000', {
	reconnectionDelayMax: 10000
});

export const sendMessage = (message: string) => {
	socket.emit('message', message);
};
