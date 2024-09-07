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
                <!-- <div v-if="allPostsPending">
                    Loading all posts...
                </div>
                <div v-if="allPosts_error">error - {{ allPosts_error }}</div>
                <ul v-else>
                    <li v-for="post in allPosts.results" :key="post.id">
                        <h1>
                            {{ post.title }}
                        </h1>
                        <h1>
                            {{ post.description }} -->
                <!-- </h1>
                    </li>
                </ul> -->

                <section class="text-gray-600 body-font overflow-hidden">
                    <div class="container px-5 py-24 mx-auto">
                        <div v-for="post in allPosts.results" :key="post.id" class="-my-8 divide-y-2 divide-gray-100">
                            <div class="py-8 flex flex-wrap md:flex-nowrap">
                                <a class="block relative h-48 rounded overflow-hidden px-8">
                                    <img alt="ecommerce" class="object-cover object-center w-full h-full block"
                                        :src=post.image>
                                </a>
                                <div class="md:flex-grow">
                                    <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">
                                        <NuxtLink :to="{ name: 'posts-id', params: { id: post.id } }">
                                            {{ post.title }}
                                        </NuxtLink>
                                    </h2>
                                    <p>{{ post.description.slice(0, 200) }} ...</p> Render post body
                                    <!-- <p>{{ post.description }} ...</p> Render post body -->
                                    <a class="text-indigo-500 inline-flex items-center mt-4">Learn More
                                        <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor"
                                            stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
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

            <!-- Single Post Section -->
            <div style="flex: 1;">
                <div v-if="singlePostStatus === 'success'">
                    <!-- Type a post ID to fetch details -->
                    <!-- <h3>{{ singlePost }}</h3> -->
                    <section class="text-gray-600 body-font">
                        <div class="container px-5 py-24 mx-auto flex flex-col">
                            <div class="lg:w-4/6 mx-auto">
                                <div class="rounded-lg h-64 overflow-hidden">
                                    <img alt="content" class="object-cover object-cover h-full w-full"
                                        src="/images/mmtasku.jpg">
                                </div>
                                <div class="flex flex-col sm:flex-row mt-10">
                                    <div class="sm:w-1/3 text-center sm:pr-8 sm:py-8">
                                        <div
                                            class="w-20 h-20 rounded-full inline-flex items-center justify-center bg-gray-200 text-gray-400">
                                            <!-- <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                    stroke-width="2" class="w-10 h-10" viewBox="0 0 24 24">
                                    <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"></path>
                                    <circle cx="12" cy="7" r="4"></circle>
                                </svg> -->
                                            <img alt="content" class="object-cover object-center h-full w-full"
                                                src="{{ singlePost.image }}">
                                        </div>
                                        <div class="flex flex-col items-center text-center justify-center">
                                            <h2 class="font-medium title-font mt-4 text-gray-900 text-lg">Author - {{
                                                singlePost.author }}
                                                Phoebe Caulfield</h2>
                                            <div class="w-12 h-1 bg-indigo-500 rounded mt-2 mb-4"></div>
                                            <p class="text-base">Author Email - {{ singlePost.author.email }} Author
                                                Email.
                                            </p>
                                        </div>
                                    </div>
                                    <div
                                        class="sm:w-2/3 sm:pl-8 sm:py-8 sm:border-l border-gray-200 sm:border-t-0 border-t mt-4 pt-4 sm:mt-0 text-center sm:text-left">
                                        <p class="leading-relaxed text-lg mb-4">{{ singlePost.description }}.</p>
                                        <!-- <a class="text-indigo-500 inline-flex items-center">
                                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                    stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                                    <path d="M5 12h14M12 5l7 7-7 7"></path>
                                </svg>
                            </a> -->
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>

                <div v-else-if="singlePostPending">
                    Loading single post...
                </div>

                <!-- <div v-else>
                    <h3>else block - {{ singlePost }}</h3>
                </div> -->
            </div>
        </div>
    </div>
</template>
