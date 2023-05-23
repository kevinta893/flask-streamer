<script lang="ts">
	import { ChevronDown } from 'svelte-heros-v2';
	import { ChevronUp } from 'svelte-heros-v2';

	export let title: string;

	let isOpen: boolean = false;
</script>

<div class="collapse rounded-md" {...$$restProps}>
	<input type="checkbox" bind:checked={isOpen} />
	<div class="collapse-title flex justify-between items-center text-xl">
		{title}
		{#if isOpen}
			<svelte:component this={ChevronDown} size={'24'} />
		{:else}
			<svelte:component this={ChevronUp} size={'24'} />
		{/if}
	</div>
	<div class="collapse-content">
		<slot />
	</div>
</div>
