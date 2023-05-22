<script lang="ts">
	export let min: number = 0;
	export let max: number = 100;
	export let value: number = 0;
	export let step: number = 5;
</script>

<input type="range" {min} {max} {step} bind:value class="range" on:change />
