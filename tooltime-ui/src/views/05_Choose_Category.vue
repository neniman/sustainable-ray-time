<template>
  <div class="main">
    <ImageHeader class="finger" :text="getText('categoryPage')" :imgPath="'kits'"/>
    <div class="categories">
      <Category 
        :class="'category-el'"
        v-for="(element, index) in categories"
        :key="index"
        :text="element.text"
        :imgPath="element.imgPath"
      />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Category from '@/components/Category.vue'
import ImageHeader from '@/components/ImageHeader.vue'

export default Vue.extend({
    name: 'Main',
    components: {
      Category,
      ImageHeader
    },
    data() {
      return {
      };
    },
    computed: {
      categories() {
        let lang = this.$store.state.language;
        let storeCategories = this.$store.state.texts[lang].category;
        let arrOfCategories = [] as any[];
        Object.keys(storeCategories).forEach((key) => { 
          arrOfCategories.push({
            text: storeCategories[key],
            imgPath: key
          });
        });
        return arrOfCategories;
      }
    },
    methods: {
        chooseTool() {
            this.$router.push('tool-detail');
        },
        getText(key) {
          return this.$store.state.texts[this.$store.state.language][key];
        }
    }
});
</script>

<style scoped>
.main {
    width: 100% !important;
    height: 92% !important;
}

.img-header {
  height: 10%;
}

.categories {
  width: 100%;
  height: 85%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  margin: 0 auto;
}

.category-el {
  width: 25% !important;
  height: 35% !important;
}
</style>