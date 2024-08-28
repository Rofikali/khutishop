import { ref } from 'vue'
import { useFetch } from '#app'

export function useFetchProducts() {
    const products = ref([])
    const product = ref(null)

    const fetchAllProducts = async () => {
        try {
            const { data } = await useFetch('/api/products')
            products.value = data.value
        } catch (error) {
            console.error('Error fetching products:', error)
        }
    }

    const fetchProductById = async (id: string) => {
        try {
            const { data } = await useFetch(`/api/products/${id}`)
            product.value = data.value
        } catch (error) {
            console.error('Error fetching product:', error)
        }
    }

    return {
        products,
        product,
        fetchAllProducts,
        fetchProductById,
    }
}
