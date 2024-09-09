// // // import { useLazyAsyncData } from '#app'

// export default function useFetchPosts() {
//     // Fetch all posts using useLazyAsyncData
//     const { status, data: posts, error } = useLazyAsyncData('posts-data', () =>
//         $fetch('/posts')
//     );

//     // Method to manually refresh posts data
//     const fetchAllPosts = async () => {
//         try {
//             console.log('Refreshing posts data...');
//             await refresh(); // Trigger a re-fetch of the data
//             console.log('Posts:', posts.value);
//         } catch (err) {
//             console.log('Error fetching posts:', err);
//         }
//     }

// geekyshows code 
//     return {
//         // Expose posts, pending state, error, and fetchAllPosts method
//         posts,
//         status,
//         error,
//         fetchAllPosts,
//     }
// }

// export default function useFetchPosts() {
//     const url = ''
//     console.log('url is here', url);
//     const posts = ref([])
//     const error = ref(null)
//     const status = ref(null)
//     const fetchAllPosts = async () => {
//         posts.value = []
//         error.value = null
//         status.value = null
//         try {
//             const res = useLazyAsyncData('posts-data', () =>
//                 $fetch('/posts')
//             );
//             console.log('response data is here', res.data)
//             posts.value = res.data
//             status.value = res.status
//         } catch (err) {
//             console.log('error is here', err)
//             error.value = err
//         }
//     }
//     return {
//         // Expose posts, pending state, error, and fetchAllPosts method
//         posts,
//         status,
//         error,
//         fetchAllPosts,
//     }
// }

import { useLazyAsyncData } from '#app'

export default function useFetchPosts() {
    // Fetch all posts using useLazyAsyncData
    const { pending, data: posts, error, refresh } = useLazyAsyncData('posts-data', () =>
        $fetch('/posts')
    );

    // Method to manually refresh posts data (fetch all posts)
    const fetchAllPosts = async () => {
        try {
            console.log('Refreshing posts data...');
            await refresh(); // Trigger a re-fetch of the data
            console.log('Posts:', posts.value);
        } catch (err) {
            console.log('Error fetching posts:', err);
        }
    }

    // Method to fetch a single post by ID
    const fetchSinglePost = async (id) => {
        try {
            console.log(`Fetching single post with ID: ${id}`);
            const singlePost = await $fetch(`/posts/${id}`); // Fetch the single post by ID
            console.log('Single Post:', singlePost);
            return singlePost; // Return the fetched single post
        } catch (err) {
            console.log('Error fetching single post:', err);
            throw err; // Handle the error appropriately
        }
    }

    return {
        posts,
        pending,
        error,
        fetchAllPosts, // Fetch all posts
        fetchSinglePost, // Fetch a single post by ID
    }
}
