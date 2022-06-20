/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./src/js/app.js":
/*!***********************!*\
  !*** ./src/js/app.js ***!
  \***********************/
/***/ ((__unused_webpack___webpack_module__, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _modules_functions_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./modules/functions.js */ \"./src/js/modules/functions.js\");\n\r\n\r\n_modules_functions_js__WEBPACK_IMPORTED_MODULE_0__.isWebp();\r\n\r\n/*Меню бургер */\r\n\r\nconst burgerOpen = document.querySelector('.header__burger');\r\nconst burgerMenu = document.querySelector('.burger__menu');\r\nconst burgerClose = document.querySelector('.burger__menu__header-btn');\r\nif (burgerOpen) {\r\n  burgerOpen.addEventListener('click', () => {\r\n    document.body.classList.toggle('_lock');\r\n    burgerMenu.classList.toggle('_active');\r\n  });\r\n}\r\nif (burgerClose) {\r\n  burgerClose.addEventListener('click', () => {\r\n    burgerMenu.classList.toggle('_active');\r\n    document.body.classList.toggle('_lock');\r\n  });\r\n}\r\n\r\nconst slider = document.querySelector('.slider');\r\nconst scrollSpeed = 3;\r\nlet isDown = false;\r\nlet startX;\r\nlet scrollLeft = 0;\r\n\r\n// EventListeners\r\nslider.addEventListener('mousedown', (e) => {\r\n  isDown = true;\r\n  slider.classList.add('dragging');\r\n  startX = e.pageX - slider.offsetLeft;\r\n  scrollLeft = slider.scrollLeft;\r\n});\r\n\r\nslider.addEventListener('mouseup', () => {\r\n  isDown = false;\r\n  slider.classList.remove('dragging');\r\n});\r\n\r\nslider.addEventListener('mouseleave', () => {\r\n  isDown = false;\r\n  slider.classList.remove('dragging');\r\n});\r\n\r\nslider.addEventListener('mousemove', (e) => {\r\n  if (!isDown) return;\r\n  e.preventDefault();\r\n  const x = e.pageX - slider.offsetLeft;\r\n  const walk = (x - startX) * scrollSpeed;\r\n  slider.scrollLeft = scrollLeft - walk;\r\n});\r\n\n\n//# sourceURL=webpack://gulp-2022/./src/js/app.js?");

/***/ }),

/***/ "./src/js/modules/functions.js":
/*!*************************************!*\
  !*** ./src/js/modules/functions.js ***!
  \*************************************/
/***/ ((__unused_webpack___webpack_module__, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"isWebp\": () => (/* binding */ isWebp)\n/* harmony export */ });\n/* Проверка поддержки webp, добавление класса webp или no-webp для HTML*/\r\nfunction isWebp() {\r\n  //Проверка поддержки webp\r\n  function testWebP(callback) {\r\n    var webP = new Image();\r\n    webP.onload = webP.onerror = function () {\r\n      callback(webP.height == 2);\r\n    };\r\n    webP.src =\r\n      'data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA';\r\n  }\r\n\r\n  //Добавление класса _webp или no-webp для HTML\r\n  testWebP(function (support) {\r\n    if (support == true) {\r\n      document.querySelector('body').classList.add('webp');\r\n    } else {\r\n      document.querySelector('body').classList.add('no-webp');\r\n    }\r\n  });\r\n}\r\n\n\n//# sourceURL=webpack://gulp-2022/./src/js/modules/functions.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = __webpack_require__("./src/js/app.js");
/******/ 	
/******/ })()
;