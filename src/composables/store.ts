import { defineStore, acceptHMRUpdate } from 'pinia'

export const useStore = defineStore("state", ()=>{
    const state = reactive({
        user: null as any,
        notifications: [] as {message: string, status: string}[],
        domain: "",
        isFetching: false,
    })

    const setState = (data: any) => {
        Object.assign(state, data)
        
}

const notify = (message:string, status:string) => {
    state.notifications.push({message, status})
}
    return {
        state,
        setState,
        notify
 
    }

})

if (import.meta.hot) {
    import.meta.hot.accept(acceptHMRUpdate(useStore, import.meta.hot))
}

