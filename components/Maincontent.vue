<template>
    <div>
        <section class="text-gray-600 body-font overflow-hidden">
            <div class="container px-5 py-24 mx-auto">
                <div v-for="post in posts" :key="post.id" class="-my-8 divide-y-2 divide-gray-100">
                    <div class="py-8 flex flex-wrap md:flex-nowrap">
                        <a class="block relative h-48 rounded overflow-hidden px-8">
                            <img alt="ecommerce" class="object-cover object-center w-full h-full block"
                                src="/images/mmta.jpg">
                        </a>
                        <div class="md:flex-grow">
                            <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">
                                <NuxtLink :to="{ name: 'posts-id', params: { id: post.id } }">
                                    {{ post.title }}
                                </NuxtLink>
                            </h2>
                            <p>{{ post.description.slice(0, 200) }} ...</p> Render post body
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
</template>

<script setup>
defineProps(['posts'])
</script>

<style lang="scss" scoped></style>