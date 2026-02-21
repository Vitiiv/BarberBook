import "vue-router";

declare module "vue-router" {
	interface RouteMeta {
		requiresAth?: boolean;
		guest?: boolean;
		roles: string[];
	}
}
