<script lang="ts">
	import Button from '$lib/component/Button.svelte';
	import Webcam from '$lib/component/Webcam.svelte';
	import { PUBLIC_WEBCAM_SERVER } from '$env/static/public';
	import { sendMessage } from '$lib/webcam/webcamControl';
	import { getWebcams } from '$lib/webcam/webcam';
	import { onMount } from 'svelte';

	let webcamIds: number[] = [];
	onMount(async () => {
		webcamIds = await getWebcams();
	});

	let counter = 0;
	const sendClick = () => {
		sendMessage(`Reporting: ${counter++}`);
	};
</script>

{#each webcamIds as webcamId}
	<Webcam videoUrl={`${PUBLIC_WEBCAM_SERVER}/webcams/${webcamId}/stream`} />
{/each}
<Button primary on:click={sendClick}>Hello counter</Button>
