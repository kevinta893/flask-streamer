<script lang="ts">
	import Button from '../lib/component/Button.svelte';
	import Webcam from '../lib/component/Webcam.svelte';
	import { PUBLIC_WEBCAM_URL } from '$env/static/public';
	import { sendMessage } from '../lib/websocket/webcamControl';

	let counter = 0;
	const sendClick = () => {
		sendMessage(`Reporting: ${counter++}`);
	};
</script>

<Webcam videoUrl={PUBLIC_WEBCAM_URL} />

<Button primary on:click={sendClick}>Hello counter</Button>
