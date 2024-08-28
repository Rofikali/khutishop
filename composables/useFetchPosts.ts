import { ref } from 'vue'
import { useFetch } from '#app'

export function useFetchPosts() {
    const posts = ref([])
    const post = ref(null)

    const fetchAllPosts = async () => {
        try {
            const { data } = await useFetch('/api/posts')
            posts.value = data.value
        } catch (error) {
            console.error('Error fetching posts:', error)
        }
    }

    const fetchPostById = async (id: string) => {
        try {
            const { data } = await useFetch(`/api/posts/${id}`)
            post.value = data.value
        } catch (error) {
            console.error('Error fetching post:', error)
        }
    }

    return {
        posts,
        post,
        fetchAllPosts,
        fetchPostById,
    }
}
