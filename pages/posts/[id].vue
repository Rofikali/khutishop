<template>
    <div v-if="post">
        <!-- <h1>Single post is here</h1>
        <h1>Title - {{ post.title }}</h1>
        <h1>Content - {{ post.description }}</h1> -->
        <Postdetail :post="post" />
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
// // Fetching the data using useLazyAsyncData
const { data: post, pending, error } = await useLazyAsyncData(() => $fetch(`/posts/${route.params.id}`))
// // const { data: post, pending, error } = await useLazyAsyncData(() => $fetch(`http://127.0.0.1:8000/posts/${route.params.id}`))
// console.log('single post ', post)


// import { onMounted } from 'vue'
// import { useRoute } from 'vue-router'
// import { useFetchPosts } from '~/composables/useFetchPosts'

// const { post, fetchPostById } = useFetchPosts()
// const route = useRoute()

// onMounted(() => {
//     fetchPostById(route.params.id)
// })
</script>

<style scoped></style>