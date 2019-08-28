'use strict';
(function imageView(){

    const imageView = document.querySelector("#django-input-image-view");
    const labelImageView = document.querySelector("#django-label-image-view")
    const imagePreview = document.querySelector("#image-container-view");
    const imageShowEdit = document.querySelector("#image-preview-edit");


     /**
      * @function createElementImg
      * @description Create a element img and add the patch
      * @param {*} element 
      * @param {*} patch 
      */
     let createElementImg = (element,patch) =>{
        const image = document.createElement("img");
        image.setAttribute("src",patch) 
        image.setAttribute("class","image-preview")       
        element.appendChild(image);        
     }

     
     /**
      * @function isNullInputs
      * @description Validate if reference is null
      * @param {*} inputReference 
      * @returns {Boolean}
      */
    let isNullInputs = (inputReference) => {
        return (inputReference == null)? true : false;
    }


    /**
     * @function getFileInput
     * @description get a input and create elment node or update the target result to img
     * @param {*} input 
     */
    let getFileInput = (input) => {
        if (input.files && input.files[0]) {
            const reader = new FileReader();
            reader.addEventListener("load",(e)=>{
                if(!isNullInputs(imageShowEdit)){
                    imageShowEdit.setAttribute('src',event.target.result)
                }else{
                    createElementImg(imagePreview,e.target.result)
                }
            });
            reader.readAsDataURL(input.files[0]);
        }
    }


     if(!isNullInputs(imageView) && !isNullInputs(labelImageView)){
        labelImageView.addEventListener('click',(event)=>{
            event.preventDefault();
            imageView.click()
        });    

        imageView.addEventListener("change",(event)=>{
            getFileInput(imageView)
        });
    }
    
})();