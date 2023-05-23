<script lang="ts">
	import { PUBLIC_WEBCAM_SERVER } from '$env/static/public';
	import Range from './Range.svelte';

	import { Play } from 'svelte-heros-v2';
	import { Pause } from 'svelte-heros-v2';
	import {
		setBrightness,
		setExposure,
		setHue,
		setPlayStatus,
		setSaturation
	} from '$lib/webcam/webcamControl';
	import Button from './Button.svelte';

	export let webcamId: number;

	$: videoUrl = `${PUBLIC_WEBCAM_SERVER}/webcams/${webcamId}/stream`;

	let playing = true;
	let brightness = 0;
	let exposure = 0;
	let saturation = 0;
	let hue = 0;

	$: setBrightness(webcamId, brightness);
	$: setExposure(webcamId, exposure);
	$: setSaturation(webcamId, saturation);
	$: setHue(webcamId, hue);

	const togglePlay = () => {
		playing = !playing;
		setPlayStatus(webcamId, playing);
	};

	const resetSettings = () => {
		brightness = 0;
		exposure = 0;
		saturation = 0;
		hue = 0;
	};
</script>

<div class="card card-compact w-96 bg-base-100 shadow-xl">
	<figure>
		<img class="select-none" src={videoUrl} alt="webcam" draggable="false" />
	</figure>
	<div class="card-body">
		<div class="card-actions justify-end">
			Brightness
			<Range min={-100} max={100} step={10} bind:value={brightness} />
			Exposure
			<Range min={-100} max={100} step={10} bind:value={exposure} />
			Saturation
			<Range min={-100} max={100} step={10} bind:value={saturation} />
			Hue
			<Range min={-100} max={100} step={10} bind:value={hue} />
			<div class="flex w-full justify-between">
				<Button on:click={resetSettings}>Reset</Button>
				<Button primary on:click={togglePlay}>
					{#if playing}
						<Pause class="select-none" />
					{:else}
						<Play class="select-none" />
					{/if}
				</Button>
			</div>
		</div>
	</div>
</div>
