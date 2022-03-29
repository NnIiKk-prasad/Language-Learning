// CommonJS, every file is module (by default)
// Modules - Encapsulated Code (only share minimum)

// Importing Custom Modules
const names = require('./01-names')
const sayHi = require('./02-utils')
const data = require('./03-alternative-syntax')
require('./04-without-exports')

sayHi('susan')
sayHi(names.john)
sayHi(names.peter)
console.log(data)