import React from 'react'
//import ReactDom from 'react-dom'
import { createRoot } from 'react-dom/client'
import './index.css'
const container = document.getElementById('root')
const root = createRoot(container) // createRoot(container!) if you use TypeScript

function BookList() {
  return (
    <section className='booklist'>
      <Book />
      <Book />
      <Book />
      <Book />
    </section>
  )
}

const Book = () => {
  return (
    <article className='book'>
      <Image></Image>
      <h1>The Very Hungry Caterpillar</h1>
      <h2
        style={{ color: '#617d98', fontSize: '0.75rem', marginTop: '0.25rem' }}
      >
        By: Eric Carle
      </h2>
      <Message />
    </article>
  )
}
const Image = () => (
  <img
    src='https://images-na.ssl-images-amazon.com/images/I/91cqEsyjd-L._AC_UL127_SR127,127_.jpg'
    alt=''
  />
)
const Message = () => {
  return (
    <p>
      A very hungry caterpillar eats and eats until the day they finally
      transform.
    </p>
  )
}
// const Greeting = () => {
//   return React.createElement('h1', {}, 'hello world')
// }
root.render(<BookList tab='home' />)
//ReactDom.render(<Greeting />, document.getElementById('root'))
