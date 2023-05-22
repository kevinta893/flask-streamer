<script lang="ts">
	import Button from '$lib/component/Button.svelte';
	import Webcam from '$lib/component/Webcam.svelte';
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

<div>
	{#each webcamIds as webcamId}
		<!-- <Draggable> -->
		<Webcam {webcamId} />
		<!-- </Draggable> -->
	{/each}
</div>

<Button primary on:click={sendClick}>Hello counter</Button>
