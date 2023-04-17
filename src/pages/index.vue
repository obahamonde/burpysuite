<script setup lang="ts">
useTitle('Burpy Suite')
const { state, notify } = useStore()
const domainRegexp = /^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$/
const response = ref({})
const domain = ref('')
const records = ref<{
domain: string
type_: string
value: string
}[]>([])


const checkDomain = async() => {
if (!domainRegexp.test(domain.value)) {
notify(`Domain ${domain.value} is not valid`, 'error')
return
}
state.domain = domain.value
response.value = {}
domain.value = ''
state.isFetching = true
const { data  } =  await useFetch(`http://localhost:8000/api/dns/${state.domain}?ref=${state.user.ref}`).json()
state.isFetching = false
response.value = unref(data)
for (const record of response.value.records) {
    const { domain, type_, value } = record
    records.value.push({ domain, type_, value })
}
}

</script>
<template>
<section col center>
<button title="Bur Py Suite">
<img src="/favicon.png" x8 hover:cp  alt="logo" class="w-1/2" />
</button>
<input type="text" v-model="domain" class="input"
@keyup.enter="checkDomain()" />
<div v-if="state.isFetching" col start>
<Loading />
</div>
<section gap-2 v-else-if="response" col center>
<br />
    <h1 text-xl font-sans underline><strong>Geolocation</strong></h1>
<p text-body><strong>City:</strong> {{ response.geo.city }}</p>
<p text-body><strong>Country:</strong> {{ response.geo.country }}</p>
<p text-body><strong>AS:</strong> {{ response.geo.org.split(' ')[0] }}</p>
<p text-body><strong>ISP:</strong> {{ response.geo.org.split(' ').slice(1).join(' ') }}</p>
<p text-body><strong>Postal Code:</strong> {{ response.geo.postal }}</p>
<p text-body><strong>Region:</strong> {{ response.geo.region }}</p>
<p text-body><strong>Timezone:</strong> {{ response.geo.timezone }}</p>
<iframe sh rounded m-4 width="500" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" :src="'https://maps.google.com/maps?ll='+response.geo.loc+'&amp;z=16&amp;output=embed'"></iframe>
<br />
<h1 text-xl font-sans underline><strong>HTTP Headers</strong></h1>
<code  text-caption w-full p-8 >
<pre lang="json"  class="bg-black p-12 w-1/2 col center mx-auto overflow-x-scroll font-mono text-success"  >{{ response.headers }}</pre>
<br />
</code>
<h1 text-xl font-sans underline><strong>DNS Records</strong></h1>
<div class="grid grid-cols-3 gap-4 mb-8">
    <div class="v-card" v-for="record in records" :key="record.domain">
<p class="v-card-text"><strong>Domain:</strong> {{ record.domain }}</p>
<p class="v-card-text"><strong>Type:</strong> {{ record.type_ }}</p>
<p class="v-card-text"><strong>Value:</strong> {{ record.value }}</p>
</div>
</div>
</section>
</section>
</template>
<style global>
.v-card {
    background-color: #fff;
    border-radius: 4px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, .15);
    transition: box-shadow .3s;
}
.v-card:hover {
    box-shadow: 0 2px 12px rgba(0, 0, 0, .2);
    cursor: none;
}
.v-card-text {
    padding: 14px 16px;
    font-size: 14px;
    color: rgba(0, 0, 0, .87);
    line-height: 20px;
}
</style>