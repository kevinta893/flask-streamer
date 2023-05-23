import { io } from 'socket.io-client';

const socket = io('ws://localhost:5000', {
	reconnectionDelayMax: 10000
});

export const sendMessage = (message: string) => {
	socket.emit('message', message);
};

export const setBrightness = (webcamId: number, brightness: number) => {
	socket.emit("brightness", { webcam: webcamId, brightness: normalizeWebcamValue(brightness) });
}
export const setExposure = (webcamId: number, exposure: number) => {
	socket.emit('exposure', { webcam: webcamId, exposure: normalizeWebcamValue(exposure) });
};
export const setSaturation = (webcamId: number, saturation: number) => {
	socket.emit('saturation', { webcam: webcamId, saturation: normalizeWebcamValue(saturation) });
}
export const setHue = (webcamId: number, hue: number) => {
	socket.emit('hue', { webcam: webcamId, hue: normalizeWebcamValue(hue) });
}

export const setPlayStatus = (webcamId: number, status: boolean) => {
	socket.emit('set_play_status', { webcam: webcamId, play: status });
}

const normalizeWebcamValue = (value: number) => value / 100;