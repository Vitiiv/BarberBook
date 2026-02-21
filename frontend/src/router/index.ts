import type { RouteRecordRaw } from "vue-router";
import { createRouter, createWebHistory } from "vue-router";


const routes: RouteRecordRaw[] = [
	{
		path: "/",
		name: "home",
		component: () => import("@/layouts/Default.vue"),
		children: [
			{
				path: "",
				name: "main",
				component: () => import("@/views/Home.vue"),
			}
		]
	},
	{
		path: "/sign-up",
		name: "sign-up",
		component: () => import("@/features/auth/views/SignUpView.vue"),
	},
	{
		path: "/sign-in",
		name: "sign-in",
		component: () => import("@/features/auth/views/SingInView.vue"),
	}
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;
