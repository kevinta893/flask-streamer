<script lang="ts">
	import Webcam from '$lib/component/Webcam.svelte';
	import { getWebcams } from '$lib/webcam/webcam';
	import { onMount } from 'svelte';

	let webcamIds: number[] = [];
	onMount(async () => {
		webcamIds = await getWebcams();
	});
</script>

<div>
	{#each webcamIds as webcamId}
		<!-- <Draggable> -->
		<Webcam {webcamId} />
		<!-- </Draggable> -->
	{/each}
</div>

