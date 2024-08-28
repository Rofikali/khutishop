// server/api/hello.ts

import { defineEventHandler } from 'h3'
import axios from 'axios'

export default defineEventHandler(async (event) => {
    try {
        // Fetch data from the Django backend
        const response = await axios.get('http://127.0.0.1:8000/posts')

        // Return the data to the frontend
        return response.data
    } catch (error) {
        // Handle errors
        return { error: 'Failed to fetch posts' }
    }
})
