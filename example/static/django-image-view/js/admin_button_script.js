'use strict';
(function imageView(){

    const imageView = document.querySelector("#django-input-image-view");
    const labelImageView = document.querySelector("#django-label-image-view")
    const imagePreview = document.querySelector("#image-container-view");
    const imageShowEdit = document.querySelector("#image-preview-edit");

    /***
     *  Utils Functions
     */

     let create_element_img = (element,patch) =>{
         /**
          * Create new Element img for show 
          */
        const image = document.createElement("img");
        image.setAttribute("src",patch) 
        image.setAttribute("class","image-preview")       
        element.appendChild(image);        
     }

    let is_null_inputs = (inputReference) => {
        /***
         *  Validate if inputs is null
         */
        if (inputReference === null){
            return true
        }
        return false
    }

    let get_file_input = (input) => {
        /**
         *  Get the data from input file
         */        
        if (input.files && input.files[0]) {
            const reader = new FileReader();
            reader.addEventListener("load",(e)=>{
                if(!is_null_inputs(imageShowEdit)){
                    imageShowEdit.setAttribute('src',event.target.result)
                }else{
                    create_element_img(imagePreview,e.target.result)
                }
            });
            reader.readAsDataURL(input.files[0]);
        }
    }

    /**
     *  Add Events
     * 
     */

     if(!is_null_inputs(imageView) && !is_null_inputs(labelImageView)){
        labelImageView.addEventListener('click',(event)=>{
            event.preventDefault();
            imageView.click()
        });    

        imageView.addEventListener("change",(event)=>{
            get_file_input(imageView)
        });
    }
    
})();