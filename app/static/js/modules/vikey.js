/*
*   ViKey : Customizable virtual keyboard
*
*   Author : Alexandre Roulois <alexandre.roulois@linguist.univ-paris-diderot.fr>
*            Laboratoire de linguistique formelle (UMR7110 CNRS/Paris-Diderot)
*            http://www.llf.cnrs.fr/Gens/Roulois
*
*   Github : https://github.com/Alex-bzh/vikey
*
*   Version 0.7b : 2016-02-15
*
*   Licence : CC BY-NC-SA 3.0 FR
*/
// When DOM is ready
$(document).ready(function() {

    /*
    *   Listeners management
    */
    // Show the virtual keyboard
    $(".vikey").click(showkbd);
    // Quit the virtual keyboard
    $(document).bind("click keydown", function(Event) {
        // If the element on which the user has clicked is not one of the VK keys
        // and if the key pressed is not the one to upper case
        if (!$(Event.target).hasClass("vk-key") & !Event.shiftKey) {
            // Just remove the whole keyboard
            $(".vk-kbd").remove();
        }
    });
    // Toggle upper/lower case
    $(document).keydown(function(Event) {
        // If SHIFT is pressed
        if (Event.shiftKey) {
            var collection = "";
            $(".vk-key").each(function() {
                collection += this.innerHTML;
            });
            var regex = new RegExp("["+ collection.toLowerCase() +"]+");
            $(".vk-key").each(function() {
                // If the keys are in lower case, we put them in upper case
                if (regex.test(this.innerHTML)) {
                    this.innerHTML = this.innerHTML.toUpperCase();
                } else {
                    this.innerHTML = this.innerHTML.toLowerCase();
                }
            });
        }
    })
    
    function showkbd(Event) {

        /*
        *   The file we want to load is deducted from the classes of the element clicked
        *   One of these values has to match the Regex ^vk-
        */
        $(this.classList).each(function() {
            if (/^vk-/.test(this)) {
                vkFile = "/static/js/modules/" + this + ".json";
            }
        });

        var customDiv = $("<div>", {
            class: "custom-keyboard-container flex justify-center" // Classe CSS personnalisée pour la div
        }).appendTo("body");



        // Ajax to communicate with the server
        $.ajax({

            // Link to the virtual keyboard you want to load
            // Adapt this line if you need a customized path
            url: vkFile,

            // What to do if the loading is a success
            success: function(vikey) {
                /*
                *   Tool. CSS class to enable the relative positioning :
                *   the ancestor element (p) becomes a reference
                */

                // OLD PROCESS
                // var ref = getPathEvent(Event)[1];
                // $(ref).addClass("vk-ref");
                // var kbd = $("<ul>", {
                //     class:"vk-kbd"
                // }).appendTo(p);
                
                // NEW PROCESS
                var kbd = $("<ul>", {
                    class: "vk-kbd"
                }).appendTo(customDiv);

                // Number of properties (lines) in the configuration file
                var nbLignes = Object.keys(vikey).length;
                // For each line
                for (var i = 0; i < nbLignes; i++) {
                    // Insertion of an unordered list into the keyboard
                    line = $("<ul>").appendTo(kbd);
                    // For each character in the current line
                    $(vikey[i]).each(function() {
                        /*
                        *   Creation of a kbd element, inside a list item,
                        *   which value is the current character.
                        *   If the current character is empty,
                        *   a CSS class 'invisible' is applied to the current item
                        *   (i.e : opacity: 0)
                        */
                        this.valueOf() == "" ?
                            $("<li>", {
                                class: "invisible"
                            }).appendTo(line)
                            :
                            $("<kbd>", {
                                class: "vk-key",
                                name: Event.target.id
                            })
                            .html(this.valueOf())
                            .appendTo(
                                $("<li>").appendTo(line)
                            );
                    });
                }

                // The position of the cursor
                var posCursor = $("#"+Event.target.id)[0].selectionStart;

                // Now, we attach listeners to all the new kbd elements
                $(".vk-key").click(function() {
                    // Which symbol?
                    var char = this.innerHTML;
                    // Where to?
                    $("#"+Event.target.id).val(function() {
                        var string;
                        if (char === "del") {
                            string = this.value.substr(0, this.value.length - 1); // Supprime le dernier caractère
                        } else {
                            string = this.value.substr(0, posCursor) + char + this.value.substr(posCursor);
                            posCursor += char.length;
                        }
                        return string;
                    });
                });

            },

            // Error message
            error: function() {
                // TODO : Générer un message d'erreur
            }

        });

    }

    /*
    *   Will be replaced by Event.path, when browsers would implement it
    *   Function used to detect the path followed by an event through DOM
    */
    // function getPathEvent(Event) {

    //     // All the variables needed
    //     var path = [];
    //     var node = Event.target;

    //     // While current element node is not <body>, we store it
    //     while (node != document.body) {
    //         path.push(node);
    //         node = node.parentNode;
    //     }

    //     // An array with all the elements nodes
    //     return path;
    // }

});
