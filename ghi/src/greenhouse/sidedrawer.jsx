import React, { useState } from 'react'
import { Typography, Drawer, Box, IconButton, Stack } from '@mui/material'
import MenuIcon from '@mui/icons-material/Menu'

const SideDrawer = () => {
    const [isDrawerOpen, setIsDrawerOpen] = useState(false)

    return (
        <>
            <IconButton
                size="large"
                edge="start"
                color="inherit"
                aria-label="logo"
                onClick={() => setIsDrawerOpen(true)}
            >
                <MenuIcon />
            </IconButton>
            <Drawer
                anchor="left"
                open={isDrawerOpen}
                onClose={() => setIsDrawerOpen(false)}
                PaperProps={{
                    style: {
                        //
                        background: `url('https://i.pinimg.com/564x/c9/25/72/c9257250a8c6bb62663db10f88545045.jpg')`,
                        backgroundSize: '325px 900px',
                        backgroundRepeat: 'no-repeat',
                    },
                }}
            >
                <Box
                    p={4}
                    width="250px"
                    textAlign={'center'}
                    role="presentation"
                    backgroundColor="#cfd6e0"
                >
                    <Typography variant="h5" component="div">
                        Menu
                    </Typography>
                </Box>
                <Stack spacing={2} p={2}>
                    <IconButton>
                        <Typography>Home</Typography>
                    </IconButton>
                    <IconButton>
                        <Typography>Greenhouse</Typography>
                    </IconButton>
                    <IconButton>
                        <Typography>Logout</Typography>
                    </IconButton>
                </Stack>
            </Drawer>
        </>
    )
}

export default SideDrawer
