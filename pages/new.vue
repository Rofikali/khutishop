<!-- <script setup>
const id = ref(1)
const { data, status } = useLazyFetch(() => `/posts/${id.value}`, {
    immediate: true
    // immediate: false
})
const pending = computed(() => status.value === 'pending');
</script>

<template>
    <div>
        <div>
            disable the input while fetching -->
<!-- <input v-model="id" type="number" :disabled="pending" />

            <div v-if="status === 'idle'">
                Type an user ID
            </div>

            <div v-else-if="pending">
                Loading ...
            </div>

            <div v-else>
                {{ data }}
            </div>
        </div>
    </div>
</template> -->

<script setup>
definePageMeta({
    layout: 'custom'
})
// Import necessary functions from Vue/Nuxt
import { ref, computed } from 'vue'

// Fetch all posts
const { data: allPosts, status: allPostsStatus, error: allPosts_error } = useLazyFetch(() => '/posts', {
    immediate: true
})
console.log('all posts', allPosts);
// Fetch a single post by ID, defaulting to the first post
const id = ref(1);
const { data: singlePost, status: singlePostStatus, error } = useLazyFetch(() => `/posts/${id.value}`, {
    immediate: true // Not fetched initially
})
console.log('single posts', singlePost);
// Track loading states
const allPostsPending = computed(() => allPostsStatus.value === 'pending');
const singlePostPending = computed(() => singlePostStatus.value === 'pending');
</script>

<template>
    <div>
        <div style="display: flex;">
            <!-- All Posts Section -->
            <div style="flex: 1;">
                <h2>All Posts</h2>
                <div v-if="allPostsPending">
                    Loading all posts...
                </div>
                <div v-if="allPosts_error">error - {{ allPosts_error }}</div>
                <ul v-else>
                    <li v-for="post in allPosts.results" :key="post.id">
                        <h1>
                            {{ post.title }}
                        </h1>
                        <h1>
                            <!-- {{ post.description }} -->
                        </h1>
                    </li>
                </ul>
            </div>

            <!-- Single Post Section -->
            <div style="flex: 1;">
                <!-- <h2>Single Post</h2> -->
                <!-- <input v-model="id" type="number" :disabled="singlePostPending" /> -->

                <!-- <div v-if="singlePostStatus === 'idle'">
                    Type a post ID to fetch details
                </div> -->
                <div v-if="singlePostStatus === 'success'">
                    <!-- Type a post ID to fetch details -->
                    <h3>{{ singlePost }}</h3>
                </div>

                <div v-else-if="singlePostPending">
                    Loading single post...
                </div>

                <div v-else>
                    <h3>{{ singlePost }}</h3>
                    <!-- <h3>{{ singlePost.title }}</h3>
                    <p>{{ singlePost.description }}</p> -->
                </div>
            </div>
        </div>
    </div>
</template>
