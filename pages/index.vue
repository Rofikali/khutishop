<!-- <template>
    <div>
        <div v-if="error">{{ error }}</div>
        <div v-else-if="status === 'pending'">pending ...</div>
        <div v-else>
            <section class="text-gray-600 body-font overflow-hidden">
                <div class="container px-5 py-24 mx-auto">
                    <div v-for="post in posts" :key="post.id" class="-my-8 divide-y-2 divide-gray-100">
                        <div class="py-8 flex flex-wrap md:flex-nowrap">
                            <div class="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
                                <span class="font-semibold title-font text-gray-700">CATEGORY</span>
                                <span class="mt-1 text-gray-500 text-sm">12 Jun 2019</span>
                            </div>
                            <div class="md:flex-grow">
                                <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">Title here ->>>>>{{
                                    post.title }}</h2>
                                <a class="text-indigo-500 inline-flex items-center mt-4">Learn More
                                    <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
                                        fill="none" stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M5 12h14"></path>
                                        <path d="M12 5l7 7-7 7"></path>
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>

<script setup>


const { status, data: posts, error } = await useLazyAsyncData(() => $fetch('https://dummyjson.com/posts?limit=10'))
console.log('posts', posts)
for (let index = 0; index < posts.length; index++) {
    const element = posts[index];
    console.log(element)
    
}
</script>

<style lang="scss" scoped></style>
// 'https://dummyjson.com/posts?limit=10&skip=10' -->


<!-- Error Handling -->
<!-- Displaying Posts -->
<!-- <template>
    <div>
        <div v-if="error">{{ error }}</div>
        <div v-else-if="status === 'pending'">pending ...</div>
        <div v-else>
            <section class="text-gray-600 body-font overflow-hidden">
                <div class="container px-5 py-24 mx-auto">
                    <div v-for="post in posts" :key="post.id" class="-my-8 divide-y-2 divide-gray-100">
                        <div class="py-8 flex flex-wrap md:flex-nowrap">
                            <a class="block relative h-48 rounded overflow-hidden px-8">
                                <img alt="ecommerce" class="object-cover object-center w-full h-full block"
                                    src="https://dummyimage.com/420x260">
                            </a>
                            <div class="md:flex-grow">
                                <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">{{ post.title }}</h2>
                                <p>{{ post.body.slice(0, 150) }} ...</p> Render post body -->
<!-- <a class="text-indigo-500 inline-flex items-center mt-4">Learn More
                                    <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
                                        fill="none" stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M5 12h14"></path>
                                        <path d="M12 5l7 7-7 7"></path>
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>

<script setup>
const { status, data, error } = await useLazyAsyncData(() => $fetch('https://dummyjson.com/posts?limit=10'))

// Access posts data directly from data.value
const posts = data.value.posts || []
console.log('posts', posts)
</script>

<style lang="scss" scoped></style> -->

<!-- 
<template>
    <div>
        Error Handling -->
<!-- <div v-if="error">{{ error }}</div>
        <div v-else-if="status === 'pending'">pending ...</div>
        <div v-else>
             Displaying Posts -->
<!-- <section class="text-gray-600 body-font overflow-hidden">
                <div class="container px-5 py-24 mx-auto">
                    <div v-for="post in posts" :key="post.id" class="-my-8 divide-y-2 divide-gray-100">
                        <div class="py-8 flex flex-wrap md:flex-nowrap">
                            <a class="block relative h-48 rounded overflow-hidden px-8">
                                <img alt="ecommerce" class="object-cover object-center w-full h-full block"
                                    src="https://dummyimage.com/420x260">
                            </a>
                            <div class="md:flex-grow">
                                <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">{{ post.title }}</h2>
                                <p>{{ post.body.slice(0, 150) }} ...</p> Render post body -->
<!-- <a class="text-indigo-500 inline-flex items-center mt-4">Learn More
                                    <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
                                        fill="none" stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M5 12h14"></path>
                                        <path d="M12 5l7 7-7 7"></path>
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div> -->
<!-- Load More Button -->
<!-- <button
                        @click="loadMorePosts"
                        class="mt-8 text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg"
                        :disabled="loadingMore"
                    >
                        {{ loadingMore ? 'Loading...' : 'Load More' }}
                    </button>
                </div>
            </section>
        </div>
    </div>
</template> -->

<!-- <script setup>
import { ref } from 'vue'

const posts = ref([])
const currentPage = ref(0)
const limit = 10
const loadingMore = ref(false)
const error = ref(null)
const status = ref('pending')

const fetchPosts = async () => {
    try {
        status.value = 'pending'
        const { posts: newPosts } = await $fetch(`https://dummyjson.com/posts?limit=${limit}&skip=${currentPage.value * limit}`)
        posts.value = [...posts.value, ...newPosts] // Append new posts to the existing list
        status.value = 'resolved'
    } catch (err) {
        error.value = 'Failed to load posts'
        status.value = 'error'
    }
}

const loadMorePosts = async () => {
    loadingMore.value = true
    currentPage.value++
    await fetchPosts()
    loadingMore.value = false
}

// Fetch the initial posts
await fetchPosts()
</script>

<style lang="scss" scoped></style> -->

<template>
    <div>
        <!-- Error Handling -->
        <div v-if="error">{{ error }}</div>
        <div v-else-if="status === 'pending'">pending ...</div>
        <div v-else>
            <!-- Displaying Posts -->
            <section class="text-gray-600 body-font overflow-hidden">
                <div class="container px-5 py-24 mx-auto">
                    <div v-for="post in posts" :key="post.id" class="-my-8 divide-y-2 divide-gray-100">
                        <div class="py-8 flex flex-wrap md:flex-nowrap">
                            <a class="block relative h-48 rounded overflow-hidden px-8">
                                <img alt="ecommerce" class="object-cover object-center w-full h-full block"
                                    src="https://dummyimage.com/420x260">
                            </a>
                            <div class="md:flex-grow">
                                <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">{{ post.title }}</h2>
                                <p>{{ post.body.slice(0, 150) }} ...</p> <!-- Render post body -->
                                <a class="text-indigo-500 inline-flex items-center mt-4">Learn More
                                    <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
                                        fill="none" stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M5 12h14"></path>
                                        <path d="M12 5l7 7-7 7"></path>
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>
                    <!-- Loading Indicator -->
                    <div ref="bottom" class="py-8 text-center text-gray-500">
                        <span v-if="loadingMore">Loading more posts...</span>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const posts = ref([])
const currentPage = ref(0)
const limit = 10
const loadingMore = ref(false)
const error = ref(null)
const status = ref('pending')
let observer

const fetchPosts = async () => {
    try {
        status.value = 'pending'
        const { posts: newPosts } = await $fetch(`https://dummyjson.com/posts?limit=${limit}&skip=${currentPage.value * limit}`)
        posts.value = [...posts.value, ...newPosts] // Append new posts to the existing list
        status.value = 'resolved'
    } catch (err) {
        error.value = 'Failed to load posts'
        status.value = 'error'
    }
}

const loadMorePosts = async () => {
    loadingMore.value = true
    currentPage.value++
    await fetchPosts()
    loadingMore.value = false
}

const handleIntersection = (entries) => {
    if (entries[0].isIntersecting && !loadingMore.value) {
        loadMorePosts()
    }
}

// Setup IntersectionObserver for infinite scroll
onMounted(() => {
    observer = new IntersectionObserver(handleIntersection)
    observer.observe(document.querySelector('#bottom')) // Observe the loading indicator
    fetchPosts()
})

onBeforeUnmount(() => {
    if (observer) {
        observer.disconnect()
    }
})
</script>

<style lang="scss" scoped></style>
