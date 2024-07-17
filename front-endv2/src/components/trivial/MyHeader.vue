<template>
    <div class="w-full  ">
        <blockquote v-if="type==='primary'" class="p-2 ml-0 border border-l-4 border-sky-300 bg-sky-50">
            <p class="text-xl font-medium  border-sky-800">
                {{ content }}
            </p>
        </blockquote>
    </div>
</template>
    
<script setup>
const props = defineProps({
    color: {
        type: String,
    },
    content: {
        type: String,
        default: ''
    },
    type:{
        type: String,
        default: 'primary'
    }
});

</script> 
    
<style scoped>
.border {
    border-left:  solid;
}

</style>