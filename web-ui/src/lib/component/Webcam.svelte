<script lang="ts">
	import { PUBLIC_WEBCAM_SERVER } from '$env/static/public';
	import Range from './Range.svelte';

	import { Play } from 'svelte-heros-v2';
	import { Pause } from 'svelte-heros-v2';
	import { setBrightness, setExposure, setHue, setSaturation } from '$lib/webcam/webcamControl';

	export let webcamId: number;

	$: videoUrl = `${PUBLIC_WEBCAM_SERVER}/webcams/${webcamId}/stream`;

	let playing = true;
	let brightness = 50;
	let exposure = 50;
	let saturation = 50;
	let hue = 50;

	$: setBrightness(webcamId, brightness);
	$: setExposure(webcamId, exposure);
	$: setSaturation(webcamId, saturation);
	$: setHue(webcamId, hue);
	const togglePlay = () => {
		playing = !playing;
	};
</script>

<div class="card card-compact w-96 bg-base-100 shadow-xl">
	<figure>
		<img class="select-none" src={videoUrl} alt="webcam" draggable="false" />
	</figure>
	<div class="card-body">
		<div class="card-actions justify-end">
			<Range bind:value={brightness} step={5} />
			<Range bind:value={exposure} step={5} />
			<Range bind:value={saturation} step={5} />
			<Range bind:value={hue} step={5} />
			<button class="btn btn-primary" on:click={togglePlay}>
				{#if playing}
					<Pause class="select-none" />
				{:else}
					<Play class="select-none" />
				{/if}
			</button>
		</div>
	</div>
</div>
