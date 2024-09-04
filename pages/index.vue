<!-- <style lang="scss" scoped></style>
// 'https://dummyjson.com/posts?limit=10&skip=10' -->

<!-- Error Handling -->
<!-- Displaying Posts -->
<template>
    <div>
        <!-- Error Handling -->
        <div v-if="error">{{ error }}</div>
        <div v-else-if="status === 'pending'">pending ...</div>
        <div v-else>
            <Maincontent :posts="posts" />
        </div>
    </div>
</template>

<script setup>
// first step 
// const { status, data: posts, error } = await useLazyAsyncData(() => $fetch('http://127.0.0.1:8000/posts'))
// second steps 
const { status, data: posts, error } = await useLazyAsyncData(() => $fetch('/posts'))
// third steps 
// import { onMounted } from 'vue'
// import { useFetchPosts } from '~/composables/useFetchPosts'

</script>

<style lang="scss" scoped></style>
