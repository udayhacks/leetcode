// Last updated: 04/04/2026, 13:11:37
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let cur = init ;
    return {
    increment: ()=>{
        return ++init;
    },
    decrement:function(){
        return --init;
    },
    reset:function(){
        init = cur;
        return init;
    }

    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */