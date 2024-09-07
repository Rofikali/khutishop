<template>
    <div v-if="post">
        <LazyPostdetail :post="post" />
    </div>
    <div v-else-if="error">
        <h1>error ... {{ error }}</h1>
    </div>
    <div v-else>
        <h1>Loading...</h1>
    </div>
</template>

<script setup>

definePageMeta({
    layout: 'custom'
})
// import { ref } from 'vue'
const route = useRoute();
// Fetching the data using useLazyAsyncData
const { data: post, pending, error } = await useLazyAsyncData(() => $fetch(`/posts/${route.params.id}`))

</script>

<style scoped></style>