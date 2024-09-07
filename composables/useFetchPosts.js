import { useLazyAsyncData } from '#app'

export default function useFetchPosts() {
    // Fetch all posts using useLazyAsyncData
    const { pending, data: posts, error, refresh } = useLazyAsyncData('posts-data', () =>
        $fetch('/posts')
    );

    // Method to manually refresh posts data
    const fetchAllPosts = async () => {
        try {
            console.log('Refreshing posts data...');
            await refresh(); // Trigger a re-fetch of the data
            console.log('Posts:', posts.value);
        } catch (err) {
            console.log('Error fetching posts:', err);
        }
    }

    return {
        // Expose posts, pending state, error, and fetchAllPosts method
        posts,
        pending,
        error,
        fetchAllPosts,
    }
}
