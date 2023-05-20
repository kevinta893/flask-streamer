<script lang="ts">
	export let primary: boolean = false;
	export let secondary: boolean = false;
</script>

<button class="btn" class:btn-primary={primary} class:btn-secondary={secondary} on:click>
	<slot />
</button>
