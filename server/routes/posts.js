// server/api/hello.ts

import { defineEventHandler } from 'h3'
import axios from 'axios'

export default defineEventHandler(async (event) => {
    try {
        // Fetch data from the Django backend
        const response = await axios.get('http://127.0.0.1:8000/posts?limit=20')
        // const response = await axios.get('http://127.0.0.1:8000/posts')

        // Return the data to the frontend
        // console.log('response from server', response.data);
        // console.log('only reslults', response.data.results[0]);
        return response.data
    } catch (error) {
        // Handle errors
        return { error: 'Failed to fetch posts' }
    }
})
