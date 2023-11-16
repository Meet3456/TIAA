import ReactDOM from 'react-dom/client'
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import App from './App.tsx'
import './index.css'
import Land from './home/land.tsx';
import Community from './mebership/Community/index.tsx';
import Planning from './mebership/Planning/index.tsx';
import { Auth0Provider } from '@auth0/auth0-react';


ReactDOM.createRoot(document.getElementById('root')!).render(
  <Auth0Provider
    domain="dev-prsbdtf063p5f8z0.us.auth0.com"
    clientId="5op4LspQrwXirf2TWp0NBpTUFs8ONEbL"
    authorizationParams={{
      redirect_uri: window.location.origin
    }}
  >
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<App />} />
        <Route path='/home' element={<Land />} />
        <Route path='/community' element={<Community />} />
        <Route path='/planning' element={<Planning />} />
      </Routes>
    </BrowserRouter>
  </Auth0Provider>
)
