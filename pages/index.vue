<!-- <style lang="scss" scoped></style>
// 'https://dummyjson.com/posts?limit=10&skip=10' -->

<!-- Error Handling -->
<!-- Displaying Posts -->
<template>
    <div>

        <div v-if="posts">
            <LazyMaincontent :posts="posts.results" />
        </div>
        <!-- Error Handling -->
        <div v-else-if="error">{{ error }}</div>
        <div v-else>pending ... {{ pending }}</div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import useFetchPosts from '~/composables/useFetchPosts'

// Ensure you have all the necessary imports
const { posts, pending, error, fetchAllPosts } = useFetchPosts()

// Fetch all posts when the component is mounted
onMounted(() => {
    fetchAllPosts()
})
</script>